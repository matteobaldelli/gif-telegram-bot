"""empty message

Revision ID: 33386f4da0c2
Revises: 
Create Date: 2018-08-01 17:58:32.706340

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '33386f4da0c2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('chat_id', sa.Integer(), nullable=True),
    sa.Column('update_date', sa.DateTime(timezone=True), nullable=True),
    sa.Column('creation_date', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
